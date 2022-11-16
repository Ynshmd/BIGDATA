from pyspark.sql import SparkSession

#sans se connecter au cluster
#spark = SparkSession.builder.getOrCreate()

spark = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "2g").\
        getOrCreate()
        
path  = ""
# lecture d'un fichier de manière la plus brute
df    = spark.read.load(path, format="csv")
df.dtypes