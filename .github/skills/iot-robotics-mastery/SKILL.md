---
name: iot-robotics-mastery
description: "Use when: studying IoT Internet of Things, learning robotics, understanding embedded systems, learning Arduino Raspberry Pi, studying ROS Robot Operating System, learning sensor actuator programming, MQTT CoAP protocols, edge computing, studying SLAM localization, autonomous systems, drone programming, learning control theory, mechatronics, IoT security, smart home systems."
argument-hint: "Topic or phase (e.g., 'MQTT protocol', 'ROS basics', 'Phase 2 robotics')"
---

# IoT & Robotics Mastery Roadmap

A structured roadmap for mastering IoT and Robotics — from embedded basics through autonomous systems.

## When to Use

- Starting or resuming an IoT or robotics journey
- Learning embedded programming (Arduino, Raspberry Pi, ESP32)
- Understanding IoT architectures and protocols
- Studying robotics (ROS, SLAM, path planning)
- Building IoT or robotics projects

---

## Phase 0: Foundations

> **Goal**: Understand electronics, embedded systems, and communication basics.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | Electronics Basics | Voltage, current, resistance, Ohm's law, digital vs analog signals, breadboards, basic circuits, pull-up/pull-down resistors |
| 0.2 | Microcontrollers | Arduino (pins, digital/analog I/O, serial), ESP32 (WiFi, Bluetooth, dual-core), Raspberry Pi (GPIO, Linux, Python), development environments |
| 0.3 | Sensors & Actuators | Temperature, humidity, ultrasonic, IR, accelerometer/gyroscope (IMU), servos, DC motors, stepper motors, motor drivers |
| 0.4 | Communication | Serial (UART), SPI, I2C, PWM — when to use each, wiring, libraries |

### Checkpoint
- Build an Arduino project that reads a sensor and controls an actuator
- Explain the difference between SPI and I2C
- Set up a Raspberry Pi to read sensor data and log it

---

## Phase 1: IoT Architecture

> **Goal**: Build connected IoT systems from device to cloud.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | IoT Architecture | Device → gateway → cloud, edge computing, fog computing, IoT reference architectures |
| 1.2 | IoT Protocols | MQTT (broker, pub/sub, QoS levels, retained messages, last will), CoAP (constrained RESTful), HTTP for IoT, WebSocket |
| 1.3 | Networking | WiFi, Bluetooth/BLE, Zigbee, LoRa/LoRaWAN, cellular (NB-IoT, LTE-M), mesh networking — range vs power vs bandwidth trade-offs |
| 1.4 | Cloud IoT | AWS IoT Core, Azure IoT Hub, Google Cloud IoT — device provisioning, telemetry ingestion, device shadows/twins, rules engine |
| 1.5 | Data Pipeline | Time-series data storage (InfluxDB, TimescaleDB), stream processing, dashboards (Grafana), alerting, analytics |
| 1.6 | IoT Security | Device authentication (X.509, SAS tokens), TLS for constrained devices, firmware updates (OTA), secure boot, physical security |

### Projects
- Smart home sensor network (temperature, humidity, motion → MQTT → dashboard)
- Remote monitoring system with alerts and historical data
- ESP32 + cloud integration with device shadow

---

## Phase 2: Robotics Fundamentals

> **Goal**: Understand how robots perceive, plan, and act.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | Robotics Overview | Types of robots (mobile, manipulator, aerial, underwater), degrees of freedom, workspace, kinematic chains |
| 2.2 | Kinematics | Forward kinematics, inverse kinematics, DH parameters, transformation matrices, homogeneous coordinates |
| 2.3 | Sensors for Robotics | LiDAR, cameras (stereo, depth), IMU, encoders, GPS, ultrasonic, sensor fusion (Kalman filter) |
| 2.4 | Control Theory | PID controller (proportional, integral, derivative), tuning, feedforward, state-space control, trajectory following |
| 2.5 | ROS (Robot Operating System) | ROS 2 architecture (nodes, topics, services, actions), publishers/subscribers, launch files, URDF, TF transforms, Gazebo simulation |

### Checkpoint
- Program a PID controller to follow a line
- Create a ROS 2 node that publishes sensor data and subscribes to commands
- Simulate a robot in Gazebo

---

## Phase 3: Autonomous Systems

> **Goal**: Build robots that perceive and navigate autonomously.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 3.1 | Computer Vision for Robotics | OpenCV basics, object detection, color tracking, depth estimation, fiducial markers (ArUco), visual odometry |
| 3.2 | Localization | Dead reckoning, wheel odometry, GPS, particle filter, Extended Kalman Filter (EKF), sensor fusion |
| 3.3 | Mapping | Occupancy grid maps, point cloud processing, 2D/3D mapping, map representations |
| 3.4 | SLAM | Simultaneous Localization and Mapping, EKF-SLAM, graph-based SLAM, RTAB-Map, ORB-SLAM |
| 3.5 | Path Planning | A*, Dijkstra's, RRT (Rapidly-exploring Random Trees), potential fields, dynamic path planning, obstacle avoidance |
| 3.6 | Multi-Robot Systems | Communication protocols, task allocation, swarm intelligence, cooperative mapping |

### Projects
- Autonomous navigation robot (SLAM + path planning in ROS)
- Drone programming with autonomous waypoint navigation
- Multi-robot coordination simulation

---

## Phase 4: Specialized Topics

> **Goal**: Go deep in a chosen specialization.

| Specialization | Topics |
|---------------|--------|
| **Drones/UAVs** | Flight dynamics, PX4/ArduPilot, MAVLink, autonomous flight, drone swarms |
| **Manipulators** | Robot arms, pick & place, force control, MoveIt (ROS), grasp planning |
| **Self-Driving** | Perception pipeline, object detection, lane detection, control, simulation (CARLA) |
| **Soft Robotics** | Compliant mechanisms, pneumatic actuators, bio-inspired design |

---

## Progress Tracking

- Save notes under `iot-robotics/` folder
- Create `iot-robotics/progress.md` to track completed modules
- Save project code and wiring diagrams

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| Arduino Docs | Reference | Arduino programming |
| ROS 2 Tutorials | Docs | ROS fundamentals |
| ESP32 Programming Guide | Docs | ESP32 IoT projects |
| Robotics: Modelling, Planning and Control (Siciliano) | Book | Robotics theory |
| Introduction to Autonomous Mobile Robots (Siegwart) | Book | Mobile robotics |
| HiveMQ MQTT Essentials | Tutorial | MQTT protocol |
