def job_sequencing(job_data):
    job_data.sort(key=lambda x: x[2], reverse=True)  # Sort jobs by profit in descending order
    max_deadline = max(job_data, key=lambda x: x[1])[1]  # Find the maximum deadline

    # Initialize the schedule array with -1, indicating an empty slot
    schedule = [-1] * max_deadline

    total_profit = 0
    for job in job_data:
        deadline, profit = job[1], job[0]

        # Find a suitable slot for the job
        for i in range(deadline - 1, -1, -1):
            if schedule[i] == -1:
                schedule[i] = profit
                total_profit += profit
                break

    return schedule, total_profit


# Get user input for job data
num_jobs = int(input("Enter the number of jobs: "))
job_data = []

for i in range(num_jobs):
    profit, deadline = map(int, input(f"Enter profit and deadline for job {i + 1} (separated by space): ").split())
    job_data.append((profit, deadline, i + 1))

# Call the job sequencing function
schedule, total_profit = job_sequencing(job_data)

# Display the schedule and total profit
print("\nJob Schedule:")
for i, profit in enumerate(schedule):
    if profit != -1:
        print(f"Job {i + 1} -> Profit: {profit}")

print(f"\nTotal Profit: {total_profit}")
