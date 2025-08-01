import customtkinter as ctk
import json, os, sys, webbrowser
from tkinter import messagebox

def load_config():
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.argv[0])))
    path = os.path.join(base, 'config.json')
    if not os.path.exists(path):
        messagebox.showerror("Error", f"config.json not found:\n{base}")
        sys.exit(1)
    try:
        cfg = json.load(open(path, 'r'))
    except Exception as e:
        messagebox.showerror("Error parsing config.json", str(e))
        sys.exit(1)
    configs = cfg.get('configs', {})
    if not configs:
        messagebox.showerror("Error", "No ‘configs’ key in config.json")
        sys.exit(1)
    # pick the first (only) game config
    return next(iter(configs.values()))

# theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class GuideApp(ctk.CTk):
    def __init__(self, game_cfg):
        super().__init__()
        self.classes = game_cfg.get('classes', {})
        if not self.classes:
            messagebox.showerror("Error", "No ‘classes’ defined in config.json")
            sys.exit(1)
        self.title("Show Guides")
        self.geometry("340x200")
        self.minsize(340, 200)
        self.resizable(True, True)
        self._build_ui()

    def _build_ui(self):
        container = ctk.CTkFrame(self)
        container.pack(fill='both', expand=True, padx=20, pady=20)
        container.grid_columnconfigure(0, weight=0)
        container.grid_columnconfigure(1, weight=1)

        # Class dropdown
        class_names = list(self.classes.keys())
        self.class_var = ctk.StringVar(value=class_names[0])
        self.class_menu = ctk.CTkOptionMenu(
            container,
            variable=self.class_var,
            values=class_names,
            command=self._on_class_change
        )
        ctk.CTkLabel(container, text="Select Class:")\
            .grid(row=0, column=0, sticky='w', padx=(0,10), pady=(0,10))
        self.class_menu.grid(row=0, column=1, sticky='ew', pady=(0,10))

        # Spec dropdown
        self.spec_var = ctk.StringVar()
        self.spec_menu = ctk.CTkOptionMenu(
            container,
            variable=self.spec_var,
            values=[]
        )
        ctk.CTkLabel(container, text="Select Spec:")\
            .grid(row=1, column=0, sticky='w', padx=(0,10), pady=(0,10))
        self.spec_menu.grid(row=1, column=1, sticky='ew', pady=(0,10))

        # Show Guides button
        ctk.CTkButton(
            container,
            text="Show Guides",
            command=self._show_guides
        ).grid(row=2, column=0, columnspan=2, pady=(10,0))

        # initialize spec dropdown
        self._on_class_change(self.class_var.get())

    def _on_class_change(self, cls):
        specs = list(self.classes.get(cls, {}).keys())
        self.spec_var.set(specs[0] if specs else "")
        self.spec_menu.configure(values=specs)

    def _show_guides(self):
        cls = self.class_var.get()
        spec = self.spec_var.get()
        urls = self.classes.get(cls, {}).get(spec, [])
        if not urls:
            messagebox.showinfo("No Guides", f"No URLs for {cls} → {spec}")
            return
        for url in urls:
            webbrowser.open(url)

if __name__ == "__main__":
    cfg = load_config()
    app = GuideApp(cfg)
    app.mainloop()
