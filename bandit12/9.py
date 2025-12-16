import subprocess
import os

f = "data"

# Convert hex dump → binary
if os.path.exists("data.txt"):
    subprocess.run(["xxd", "-r", "data.txt", "data"])

while True:
    out = subprocess.check_output(["file", f]).decode()
    print(out.strip())

    # ---------- TEXT ----------
    if "text" in out:
        with open(f, "r", errors="ignore") as fp:
            first_line = fp.readline()

            if first_line.startswith("00000000:"):
                subprocess.run(["xxd", "-r", f, "data"])
                f = "data"
                continue
            else:
                fp.seek(0)
                print(fp.read())
                break

    # ---------- GZIP ----------
    elif "gzip compressed" in out:
        os.rename(f, f + ".gz")
        f += ".gz"
        subprocess.run(["gunzip", f])
        f = f[:-3]

    # ---------- BZIP2 ----------
    elif "bzip2 compressed" in out:
        os.rename(f, f + ".bz2")
        f += ".bz2"
        subprocess.run(["bunzip2", f])
        f = f[:-4]

    # ---------- TAR (FIXED) ----------
    elif "tar archive" in out:
        members = subprocess.check_output(["tar", "-tf", f]).decode().splitlines()
        subprocess.run(["tar", "-xf", f])
        f = members[0]

    else:
        print("Unknown format")
        break
