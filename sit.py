# Given parameters
size_x_um = 100.0      # Size in x-direction in micrometers
PML_UM = 10.0          # PML layer thickness in micrometers
SUBSTRATE_UM = 5.0     # Substrate thickness in micrometers
ADDITIONAL_TERM = 3.0  # Any additional term in micrometers

# Calculate position
position = -0.5 * size_x_um + PML_UM + SUBSTRATE_UM + ADDITIONAL_TERM

print("Calculated Position:", position)
