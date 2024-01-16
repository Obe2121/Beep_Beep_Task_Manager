import tkinter as tk

from tkinter import simpledialog

import json

class TaskManager:
    def __init__(self, root):
        self.root = root

        self.tasks = []

        self.load_tasks()

        # Remove title and borders
        self.root.title("Task Manager")

        self.root.overrideredirect(True)

        # Set the window size and position
        self.root.geometry("350x600+1+1")  # Adjust the size as needed

        # Create a Frame for the sidebar
        self.sidebar_frame = tk.Frame(self.root, bg='black', width=10)

        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the task listbox and other widgets (similar to your original code)
        self.task_listbox = tk.Listbox(self.root, fg='white', bg='black', font=("Arial", 11))

        self.task_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        #Make the Window Always on Top
        self.root.wm_attributes("-topmost", True)
         

        self.task_entry = tk.Entry(self.root, fg='white', bg='black', font=("Arial", 13))

        self.task_entry.pack(fill=tk.X, padx=5, pady=5)

 
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Arial", 13))

        self.add_button.pack(fill=tk.X, padx=5, pady=5)

 
        self.move_up_button = tk.Button(self.root, text="Move Up", command=self.move_up, font=("Arial", 13))

        self.move_up_button.pack(fill=tk.X, padx=5, pady=5)

 
        self.move_down_button = tk.Button(self.root, text="Move Down", command=self.move_down, font=("Arial", 13))

        self.move_down_button.pack(fill=tk.X, padx=5, pady=5)


        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, font=("Arial", 13))

        self.delete_button.pack(fill=tk.X, padx=5, pady=5)


        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task, font=("Arial", 13))

        self.edit_button.pack(fill=tk.X, padx=5, pady=5)

 
        self.update_listbox()

    def toggle_sidebar(self):
        if self.sidebar_frame.winfo_ismapped():
            self.sidebar_frame.grid_remove()
        else:
            self.sidebar_frame.grid()

    def add_task(self):

        task = self.task_entry.get()

        if task:

            self.tasks.append(task)

            self.update_listbox()

            self.task_entry.delete(0, tk.END)

            self.save_tasks()

 

    def delete_task(self):

        task_index = self.task_listbox.curselection()

        if task_index:

            del self.tasks[task_index[0]]

            self.update_listbox()

            self.save_tasks()

 

    def edit_task(self):

        task_index = self.task_listbox.curselection()

        if task_index:

            task = self.tasks[task_index[0]]

            new_task = simpledialog.askstring("Edit task", "Edit task:", initialvalue=task)

            if new_task:

                self.tasks[task_index[0]] = new_task

                self.update_listbox()

                self.save_tasks()

 

    def move_up(self):

        task_index = self.task_listbox.curselection()

        if task_index and task_index[0] > 0:

            self.tasks.insert(task_index[0]-1, self.tasks.pop(task_index[0]))

            self.update_listbox()

            self.task_listbox.select_set(task_index[0]-1)

            self.save_tasks()

 

    def move_down(self):

        task_index = self.task_listbox.curselection()

        if task_index and task_index[0] < len(self.tasks) - 1:

            self.tasks.insert(task_index[0]+1, self.tasks.pop(task_index[0]))

            self.update_listbox()

            self.task_listbox.select_set(task_index[0]+1)

            self.save_tasks()

 

    def save_tasks(self):

        with open("tasks.json", "w") as file:

            json.dump(self.tasks, file)

 

    def load_tasks(self):

        try:

            with open("tasks.json", "r") as file:

                self.tasks = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):

            self.tasks = []

 

    def update_listbox(self):

        self.task_listbox.delete(0, tk.END)

        for task in self.tasks:

            self.task_listbox.insert(tk.END, task)

 

if __name__ == "__main__":

    root = tk.Tk()

    task_manager = TaskManager(root)

    root.lift()

    root.mainloop()