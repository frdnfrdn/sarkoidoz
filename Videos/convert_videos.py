import os
import subprocess
import sys

# Переходим в папку со скриптом
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Список видео для конвертации
videos_to_convert = ['video6.MOV']

print("Начинаю конвертацию видео из MOV в MP4...")
print("=" * 50)

for video in videos_to_convert:
    if os.path.exists(video):
        output_file = video.replace('.MOV', '.mp4')
        print(f"\nКонвертирую: {video} -> {output_file}")
        
        # Путь к ffmpeg в conda (найденный ранее)
        ffmpeg_path = r'C:\Python\envs\masha_env\Library\bin\ffmpeg.exe'
        
        # Команда ffmpeg для конвертации (простое копирование без перекодирования)
        command = [
            ffmpeg_path, 
            '-i', video,           # входной файл
            '-c', 'copy',          # копировать потоки без перекодирования
            '-y',                  # перезаписать если файл существует
            output_file
        ]
        
        try:
            # Запускаем конвертацию
            result = subprocess.run(command, 
                                  capture_output=True, 
                                  text=True, 
                                  check=True)
            print(f"✅ Успешно: {output_file}")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Ошибка при конвертации {video}:")
            print(f"Код ошибки: {e.returncode}")
            if e.stderr:
                print(f"Детали: {e.stderr}")
                
        except FileNotFoundError:
            print(f"❌ ffmpeg не найден! Убедитесь что:")
            print("1. Активировано conda base окружение")
            print("2. Установлен ffmpeg: conda install -c conda-forge ffmpeg")
            sys.exit(1)
            
    else:
        print(f"⚠️  Файл не найден: {video}")

print("\n" + "=" * 50)
print("Конвертация завершена!")

# Показываем результат
print("\nФайлы в папке:")
for file in sorted(os.listdir('.')):
    if file.endswith(('.MOV', '.mp4', '.MP4')):
        size = os.path.getsize(file) / (1024*1024)  # размер в МБ
        print(f"  {file} ({size:.1f} МБ)")
