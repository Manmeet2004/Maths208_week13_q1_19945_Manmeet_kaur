from scipy.stats import norm

# Given parameters
mean_length = 10.3  # mean in cm
std_deviation = 0.65  # standard deviation in cm

# Function to calculate the percentage below a certain length in a normal distribution
def percentage_below(length, mean, std_dev):
    return norm.cdf(length, loc=mean, scale=std_dev) * 100

# a. Percentage of lengths less than 9cm
percentage_a = percentage_below(9, mean_length, std_deviation)
print(f"a. Percentage of lengths less than 9cm: {percentage_a:.2f}%")

# b. Percentage of lengths between 9.5cm and 10.6cm
percentage_b = norm.cdf(10.6, loc=mean_length, scale=std_deviation) - norm.cdf(9.5, loc=mean_length, scale=std_deviation)
print(f"b. Percentage of lengths between 9.5cm and 10.6cm: {percentage_b:.2f}%")

# c. Minimum length for the top 20%
top_20_percentage = 100 - 20
min_length_top_20 = norm.ppf(top_20_percentage / 100, loc=mean_length, scale=std_deviation)
print(f"c. Minimum length for the top 20%: {min_length_top_20:.2f}cm")
