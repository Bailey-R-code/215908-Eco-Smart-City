# List to store energy sources
energy_sources = []

def add_energy_source(source_type, production_rate):
    """
    Adds a new energy source to the energy_sources list.
    source_type: The type of energy source 'Solar', 'Wind'.
    production_rate: The production rate of the energy source in units.
    """
    # This contains the type and production rate of the new energy source
    energy_sources.append({'type': source_type, 'production_rate': production_rate})
    # Print message confirming the addition of the energy source
    print(f"Added {source_type} with production rate {production_rate} units.")

def remove_energy_source(index):
    """
    Removes an energy source from the energy_sources list by index.
    index: Energy source to be removed.
    """
    if 0 <= index < len(energy_sources):
        # Removed source's type
        removed_source = energy_sources.pop(index)
        print(f"Removed {removed_source['type']} from the energy sources.")
    else:
        # Print an error message if the index is invalid
        print("Please enter a valid index.")

def calculate_distribution(current_demand):
    """
    Calculates how much energy can be distributed based on current demand.
    current_demand: The amount of energy required to meet the demand.
    Returns the amount of energy that can be distributed.
    """
    # Calculate the total energy production from all sources
    total_production = sum(source['production_rate'] for source in energy_sources)
    print(f"Total energy production: {total_production} units")

    if total_production >= current_demand:
        # If production meets or exceeds demand, return the full demand
        print(f"Energy demand of {current_demand} units met!")
        return current_demand
    else:
        # If production is less than demand, return the total production
        print(f"Only {total_production} units available for distribution; "
              f"demand of {current_demand} units not met.")
        return total_production
