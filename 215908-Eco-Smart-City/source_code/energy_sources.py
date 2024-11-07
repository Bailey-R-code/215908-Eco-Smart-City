class EnergySource:
    """Represents an energy source with a production rate and optional description."""
    
    def __init__(self, source_type, production_rate, description=None):
        self.source_type = source_type
        self.production_rate = production_rate
        self.description = description or f"{source_type} energy source."

    def __str__(self):
        return f"{self.source_type} (Production Rate: {self.production_rate} units)"

    def update_production_rate(self, new_rate):
        """Updates the production rate of the energy source."""
        self.production_rate = new_rate
        print(f"Updated {self.source_type} production rate to {self.production_rate} units.")


class DistributionGrid:
    """Manages energy distribution from various sources."""
    
    def __init__(self):
        self.energy_sources = []

    def add_energy_source(self, source_type, production_rate, description=None):
        """Adds a new energy source to the grid."""
        energy_source = EnergySource(source_type, production_rate, description)
        self.energy_sources.append(energy_source)
        print(f"Added: {energy_source}")

    def remove_energy_source(self, index):
        """Removes an energy source from the grid by index."""
        if 0 <= index < len(self.energy_sources):
            removed_source = self.energy_sources.pop(index)
            print(f"Removed: {removed_source}")
        else:
            print("Error: Invalid index.")

    def calculate_distribution(self, current_demand):
        """Calculates how much energy can be distributed based on current demand."""
        total_production = sum(source.production_rate for source in self.energy_sources)
        print(f"Total energy production: {total_production} units")
        return min(total_production, current_demand)
