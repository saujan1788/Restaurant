# Use an official OpenJDK image with JDK
FROM openjdk:11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Compile the application
RUN javac -d /app Hello.java

# Run the application when the container launches
CMD ["java", "-cp", "/app", "MicroService.Hello"]


