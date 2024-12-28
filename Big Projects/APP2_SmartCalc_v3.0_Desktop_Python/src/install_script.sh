#!/bin/bash

# Установочные директории
INSTALL_DIR="/Applications/CalculatorApp"
BIN_DIR="/usr/local/bin"
DESKTOP_DIR="$HOME/Desktop"
APP_NAME="CalculatorApp"
APP_SCRIPT="main.py"
PYTHON_PATH=$(which python3)

# Создание директорий
echo "Создаём директории..."
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

# Копирование файлов
echo "Копируем файлы в $INSTALL_DIR..."
cp -R frontend "$INSTALL_DIR/"
cp -R backend "$INSTALL_DIR/"
cp history.json "$INSTALL_DIR/"
cp model.py "$INSTALL_DIR/"
cp "$APP_SCRIPT" "$INSTALL_DIR/"
cp presenter.py "$INSTALL_DIR/"

# Компиляция и создание libcalc.dylib
echo "Компиляция и создание libcalc.dylib..."
cd "$INSTALL_DIR"
g++ -arch x86_64h -std=c++17 -fPIC -c backend/s21_calc_model.cpp -o s21_calc_model.o
g++ -arch x86_64h -dynamiclib -o libcalc.dylib s21_calc_model.o
cd -

# Создание символической ссылки
echo "Создаём символическую ссылку в $BIN_DIR..."
ln -sf "$INSTALL_DIR/$APP_SCRIPT" "$BIN_DIR/$APP_NAME"

# Создание приложения .app
APP_DIR="$INSTALL_DIR/$APP_NAME.app"
mkdir -p "$APP_DIR/Contents/MacOS"
mkdir -p "$APP_DIR/Contents/Resources"

# Копирование иконки в Resources
cp "$INSTALL_DIR/frontend/icon.icns" "$APP_DIR/Contents/Resources/icon.icns"

# Создание скрипта для запуска Python
cat > "$APP_DIR/Contents/MacOS/$APP_NAME" <<EOL
#!/bin/bash
exec &> /tmp/${APP_NAME}_error.log
$PYTHON_PATH $INSTALL_DIR/$APP_SCRIPT
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
echo "Создаём ярлык на рабочем столе..."
ln -sf "$APP_DIR" "$DESKTOP_DIR/$APP_NAME"

echo "Установка завершена."
