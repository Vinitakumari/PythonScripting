import random

def create_sample_log(filename):
    log_levels = ['ERROR','INFO','WARNING','DEBUG']
    with open(filename , 'w') as f:
        for i in range(1000):
            level = random.choice(log_levels)
            f.write(f"2024-06-26 {i:04d}-{level}: Sample log message {i}\n")


# Create a sample log file
log_filename = 'app.log'
create_sample_log(log_filename)

print(f"sample log file'{log_filename}")