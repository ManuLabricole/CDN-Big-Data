# Launch python console
#### run python3

# Import
#### run from pyspark import SparkConf, SparkContext

# Set the appropriate binding address for the sparkDriver
#### run conf = SparkConf().set("spark.driver.bindAddress", "127.0.0.1")

# Get or create the SparkContext with the modified configuration
#### sc = SparkContext.getOrCreate(conf=conf)

# Adjust the logging level if desired (optional)
#### sc.setLogLevel("WARN")

# Verify that the Spark web interface is started
#### print("Spark Web UI: http://localhost:4040")

# ... your Spark operations here ...

# Stop the SparkContext when you're done
#### sc.stop()
