import streamlit as st

def job_sequencing_greedy(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort by profit in descending order
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    sequence = [0] * max_deadline
    total_profit = 0

    for job in jobs:
        deadline = job[1]
        for i in range(deadline - 1, -1, -1):
            if sequence[i] == 0:
                sequence[i] = job[0]
                total_profit += job[2]
                break

    return sequence, total_profit

def job_sequencing_knapsack(jobs, max_deadline):
    jobs.sort(key=lambda x: x[2] / x[1], reverse=True)  # Sort by profit-to-deadline ratio in descending order
    dp = [0] * (max_deadline + 1)

    for job in jobs:
        deadline = job[1]
        for j in range(deadline, 0, -1):
            if dp[j] == 0:
                dp[j] = job[2]
            else:
                dp[j] = max(dp[j], dp[j - 1] + job[2])

    return dp[max_deadline]

def main():
    st.title("Job Sequencing Problem Solver")

    algorithm = st.radio("Select Algorithm", ("Greedy", "Knapsack"))

    num_jobs = st.number_input("Enter number of jobs", min_value=1, step=1, value=1)

    jobs = []
    max_deadline = 0

    for i in range(num_jobs):
        job_id = st.text_input(f"Job {i+1} ID")
        deadline = st.number_input(f"Job {i+1} Deadline", min_value=1, step=1)
        profit = st.number_input(f"Job {i+1} Profit", min_value=0, step=1)
        jobs.append((job_id, deadline, profit))
        max_deadline = max(max_deadline, deadline)

    if st.button("Solve"):
        if algorithm == "Greedy":
            sequence, total_profit = job_sequencing_greedy(jobs)
            st.write("Greedy Algorithm:")
            st.write("Job Sequence:", sequence)
            st.write("Total Profit:", total_profit)
        elif algorithm == "Knapsack":
            total_profit = job_sequencing_knapsack(jobs, max_deadline)
            st.write("Knapsack Algorithm:")
            st.write("Total Profit:", total_profit)

if __name__ == "__main__":
    main()
