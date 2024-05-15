import os
import tkinter as tk
from tkinter import messagebox
import shutil

def apply_permissions_and_replace_files():
    try:
        # Construct absolute paths for System32 and SysWOW64 directories
        system32_path = os.path.join(os.environ['SystemRoot'], 'System32')
        syswow64_path = os.path.join(os.environ['SystemRoot'], 'SysWOW64')

        # Construct absolute file paths
        dll_file_system32 = os.path.join(system32_path, 'Windows.ApplicationModel.Store.dll')
        dll_file_syswow64 = os.path.join(syswow64_path, 'Windows.ApplicationModel.Store.dll')

        # Set permissions for Windows.ApplicationModel.Store.dll inside System32
        os.system('icacls "%s" /grant Everyone:(F)' % dll_file_system32)

        # Set permissions for Windows.ApplicationModel.Store.dll inside SysWOW64
        os.system('icacls "%s" /grant Everyone:(F)' % dll_file_syswow64)

        # Move or replace files
        shutil.copyfile("System32/Windows.ApplicationModel.Store.dll", dll_file_system32)
        shutil.copyfile("SysWOW64/Windows.ApplicationModel.Store.dll", dll_file_syswow64)

        messagebox.showinfo("Success", "Minecraft Bedrock Hacked successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create GUI
root = tk.Tk()
root.title("MCBTTweaker by Psycho")
root.geometry("300x100")

apply_button = tk.Button(root, text="Apply", command=apply_permissions_and_replace_files)
apply_button.pack(pady=20)

root.mainloop()