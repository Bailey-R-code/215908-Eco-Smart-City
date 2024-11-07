import tkinter as tk
from tkinter import messagebox, font  

class EnergySource:
    """Represents an energy source."""

    def __init__(self, source_type, production_rate):
        self.source_type = source_type
        self.production_rate = production_rate

    def __str__(self):
        return f"{self.source_type} (Production Rate: {self.production_rate} units)"


class DistributionGrid:
    """Manages energy sources."""

    def __init__(self):
        self.energy_sources = []

    def add_energy_source(self, source_type, production_rate):
        """Add a new energy source."""
        source = EnergySource(source_type, production_rate)
        self.energy_sources.append(source)
        return source

    def remove_energy_source(self, index):
        """Remove an energy source by index."""
        if 0 <= index < len(self.energy_sources):
            return self.energy_sources.pop(index)
        return None

    def calculate_distribution(self, current_demand):
        """Check if energy production meets current demand."""
        total_production = sum(source.production_rate for source in self.energy_sources)
        return total_production >= current_demand, total_production


class EnergySimulatorApp:
    """GUI for managing energy sources and distribution."""

    def __init__(self, root):
        self.grid = DistributionGrid()

        # GUI Components
        self.root = root
        self.root.title("Energy Distribution System")

        # Set font
        self.default_font = font.Font(family="Arial", size=12)

        self.source_type_var = tk.StringVar(value='Solar')
        self.production_rate_var = tk.DoubleVar(value=0)
        self.current_demand_var = tk.DoubleVar(value=0)

        # Energy Source Type
        tk.Label(root, text="Energy Source Type:", font=self.default_font).grid(row=0, column=0, padx=5, pady=5)
        tk.OptionMenu(root, self.source_type_var, 'Solar', 'Wind', 'Hydro').grid(row=0, column=1, padx=5, pady=5)

        # Production Rate
        tk.Label(root, text="Production Rate:", font=self.default_font).grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.production_rate_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(root, text="Add Energy Source", command=self.add_energy_source, font=self.default_font).grid(row=2, columnspan=2, pady=10)

        # Current Demand
        tk.Label(root, text="Current Demand:", font=self.default_font).grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.current_demand_var).grid(row=3, column=1, padx=5, pady=5)

        tk.Button(root, text="Calculate Distribution", command=self.calculate_distribution, font=self.default_font).grid(row=4, columnspan=2, pady=10)

        # Energy Sources List
        tk.Label(root, text="Energy Sources:", font=self.default_font).grid(row=5, column=0, padx=5, pady=5)
        self.source_listbox = tk.Listbox(root, width=50, height=10)
        self.source_listbox.grid(row=5, column=1, padx=5, pady=5)

        tk.Button(root, text="Remove Selected Source", command=self.remove_energy_source, font=self.default_font).grid(row=6, columnspan=2, pady=10)

        # Add padding to the overall window
        self.root.config(padx=10, pady=10)

    def add_energy_source(self):
        """Add an energy source based on user input."""
        try:
            source_type = self.source_type_var.get()
            production_rate = self.production_rate_var.get()

            if production_rate <= 0:
                raise ValueError("Production rate must be greater than 0.")
            
            # Add the energy source to the grid
            source = self.grid.add_energy_source(source_type, production_rate)
            self.source_listbox.insert(tk.END, str(source))
            messagebox.showinfo("Success", f"Added: {source}")

        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred.")

    def remove_energy_source(self):
        """Remove the selected energy source from the list."""
        try:
            selected_index = self.source_listbox.curselection()
            if not selected_index:
                raise ValueError("Please select an energy source to remove.")
            
            removed_source = self.grid.remove_energy_source(selected_index[0])
            self.source_listbox.delete(selected_index)
            messagebox.showinfo("Success", f"Removed: {removed_source}")

        except ValueError as e:
            messagebox.showwarning("Warning", str(e))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred.")

    def calculate_distribution(self):
        """Calculate the energy distribution based on current demand."""
        try:
            current_demand = self.current_demand_var.get()

            if current_demand <= 0:
                raise ValueError("Demand must be a positive number.")

            # Calculate the total production and check if demand is met
            meets_demand, total_production = self.grid.calculate_distribution(current_demand)
            
            if meets_demand:
                messagebox.showinfo("Distribution", f"Energy demand met! Total production: {total_production} units.")
            else:
                messagebox.showinfo("Distribution", f"Energy demand not met. Total production: {total_production} units.")

        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred while calculating distribution.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EnergySimulatorApp(root)
    root.mainloop()
