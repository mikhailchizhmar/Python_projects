#!/bin/bash

# Переменные
APP_NAME="CalculatorApp"
VERSION="1.0"
INSTALL_LOCATION="/Applications/CalculatorApp"
PKG_ID="com.example.calculatorapp"
PYTHON_PATH=$(which python3)

# Создание временной директории
echo "Создаём временную директорию..."
BUILD_DIR=$(mktemp -d -t ${APP_NAME}_pkg)
echo "Временная директория: $BUILD_DIR"

# Копирование файлов в временную директорию
echo "Копируем файлы в временную директорию..."
mkdir -p "${BUILD_DIR}${INSTALL_LOCATION}"
cp -R frontend "${BUILD_DIR}${INSTALL_LOCATION}"
cp -R backend "${BUILD_DIR}${INSTALL_LOCATION}"
cp history.json "${BUILD_DIR}${INSTALL_LOCATION}"
cp model.py "${BUILD_DIR}${INSTALL_LOCATION}"
cp main.py "${BUILD_DIR}${INSTALL_LOCATION}"
cp presenter.py "${BUILD_DIR}${INSTALL_LOCATION}"
#cp icon.icns "${BUILD_DIR}${INSTALL_LOCATION}"  # Копируем иконку

# Компиляция и создание libcalc.dylib
echo "Компиляция и создание libcalc.dylib..."
cd "${BUILD_DIR}${INSTALL_LOCATION}"
g++ -arch x86_64h -std=c++17 -fPIC -c backend/s21_calc_model.cpp -o s21_calc_model.o
g++ -arch x86_64h -dynamiclib -o libcalc.dylib s21_calc_model.o
cd -

# Создание символической ссылки
echo "Создаём символическую ссылку во временной директории..."
mkdir -p "${BUILD_DIR}/usr/local/bin"
ln -sf "${INSTALL_LOCATION}/main.py" "${BUILD_DIR}/usr/local/bin/$APP_NAME"

# Создание приложения .app
APP_DIR="${BUILD_DIR}${INSTALL_LOCATION}/$APP_NAME.app"
mkdir -p "$APP_DIR/Contents/MacOS"
mkdir -p "$APP_DIR/Contents/Resources"

# Копирование иконки в Resources
cp "${BUILD_DIR}${INSTALL_LOCATION}/frontend/icon.icns" "$APP_DIR/Contents/Resources/icon.icns"

# Создание скрипта для запуска Python
cat > "$APP_DIR/Contents/MacOS/$APP_NAME" <<EOL
#!/bin/bash
exec &> /tmp/${APP_NAME}_error.log
$PYTHON_PATH ${INSTALL_LOCATION}/main.py
EOL
chmod +x "$APP_DIR/Contents/MacOS/$APP_NAME"

# Создание Info.plist
cat > "$APP_DIR/Contents/Info.plist" <<EOL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>$APP_NAME</string>
    <key>CFBundleExecutable</key>
    <string>$APP_NAME</string>
    <key>CFBundleIdentifier</key>
    <string>com.example.$APP_NAME</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleIconFile</key>
    <string>icon.icns</string>
</dict>
</plist>
EOL

# Создание ярлыка на рабочем столе
DESKTOP_DIR="$HOME/Desktop"
mkdir -p "${BUILD_DIR}${DESKTOP_DIR}"
ln -sf "${INSTALL_LOCATION}/$APP_NAME.app" "${BUILD_DIR}${DESKTOP_DIR}/$APP_NAME"

# Создание пакета с использованием pkgbuild
echo "Создаём установочный пакет..."
pkgbuild --root "${BUILD_DIR}" \
         --identifier "${PKG_ID}" \
         --version "${VERSION}" \
         --install-location / \
         "${APP_NAME}-${VERSION}.pkg"

# Удаление временной директории
echo "Удаляем временную директорию..."
rm -rf "${BUILD_DIR}"

echo "Пакет создан: ${APP_NAME}-${VERSION}.pkg"
