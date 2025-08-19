Simulation-of-an-Online-Taxi-Service-Using-Python
A vectorized simulation of a ride-hailing service (like Uber) built from the ground up using NumPy. This project models driver allocation, trip pricing, and dynamic traffic conditions without using Pandas, focusing on efficient matrix operations.

📖 Project Overview
This project implements a core engine for a ride-hailing service. It processes user requests, dynamically allocates the nearest available driver, calculates fares based on real-time traffic, and generates comprehensive business reports. The entire simulation is built using vectorized NumPy operations for optimal performance, explicitly avoiding the use of for and while loops where possible.

🛠️ Tech Stack
Language: Python
Core Library: NumPy - For all data manipulation and vectorized calculations
Secondary Library: math - For necessary mathematical functions (e.g., ceil, sin)

🧮 Core Simulation Mechanics
The system is built around three main matrices:
user_matrix: Base information for all users (drivers and passengers).
Columns: [user_id, gender, user_type]
user_type: 0 for passenger, 1 for driver.

driver_matrix: Dynamic state of available drivers at the start of each time interval.
Columns: [driver_id, x_pos, y_pos, available_after_time]

trip_matrix: All ride requests. The core simulation updates this matrix by assigning drivers.
Columns: [request_id, passenger_id, request_time, start_x, start_y, end_x, end_y, assigned_driver_id]

assigned_driver_id is 0 initially and gets updated by the allocation algorithm.

Key Calculations:
Distance: Calculated either as Euclidean or Manhattan (user's choice).

Trip Duration: ceil( distance * traffic_rate(t) )

Traffic Rate: Dynamically varies with time: sin(t/1000) * 0.016 + 0.08

Trip Fare: ceil(cos(duration/12)) * 50 + 200 ) * duration

Driver Allocation:
The nearest available driver (based on chosen distance metric) is assigned to each open trip request.

🚀 Features & Functionality
An interactive menu (report()) provides the following analytical reports:

1. Trip Matrix at Time t: Displays the state of all trips at a specified time.

2. Cumulative Revenue at Time t: Total fares collected up to a specific time.

3. Golden Customer: Finds the passenger with the highest total travel time.

4. Most Active Driver: Finds the driver with the highest total distance traveled.

5. Most Expensive Trip: Finds the single most costly trip and its details.

6. Lost Demand Percentage: Calculates the percentage of unfulfilled trip requests.

7. Geographical Demand Distribution: Splits the map into quadrants (A, B, C, D) and reports the percentage of requests originating in each.

8. A-to-C Traveler: Finds the passenger who most frequently started trips in quadrant A and ended in quadrant C.

🏃‍♂️ How to Run the Code
Clone the repository:
git clone https://github.com/Kasra-Shah/Simulation-of-an-Online-Taxi-Service-Using-Python.git
cd ride-hailing-simulation
Install required packages:
pip install numpy
Run the main script: The core matrices are defined within the provided Asg_numpy.py file.
python Asg_numpy.py
Use the menu: The report() function will launch an interactive menu. First, choose your distance metric (Euclidean/Manhattan), then select from the report options.

📁 Repository Structure
text
ride-hailing-simulation/
├── Online-Taxi.py              # Main script containing matrix definitions and all functions
└── README.md                 # This file

⚡ Performance Note
This project is a demonstration of vectorized programming in NumPy. By avoiding explicit loops and leveraging NumPy's optimized C-backend for array operations, the simulation achieves significant performance gains, making it suitable for handling large-scale data typical in ride-hailing services.

👨‍💻 Author
Kasra Shahriari

📜 License
This project was created for an academic assignment in Numerical Programming.
