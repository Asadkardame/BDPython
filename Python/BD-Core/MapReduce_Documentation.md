
```markdown
# MapReduce Job Execution Documentation

This documentation provides step-by-step procedures to execute a MapReduce job in the Hadoop cluster.

## Step 1: Create Mapper and Reducer Scripts

Create two Python scripts named `mapper.py` and `reducer.py` using the `nano` text editor:

```bash
nano mapper.py
nano reducer.py
```

## Step 2: Prepare Input Data

Create or obtain the input data file (`data.txt`) using the `nano` text editor:

```bash
nano data.txt
```

## Step 3: Execute Map Task

Run the mapper script on the input data using the `cat` command and pipe it to `python mapper.py`:

```bash
cat data.txt | python mapper.py
```

## Step 4: Execute Map and Reduce Tasks

Run the mapper script, sort the output, and then run the reducer script using the following commands:

```bash
cat data.txt | python mapper.py | sort -k1,1 | python reducer.py
```

## Step 5: Set Execution Permissions

Ensure that the mapper and reducer scripts have executable permissions:

```bash
chmod 777 mapper.py reducer.py
```

## Step 6: Upload Input Data to HDFS

Create directories in HDFS, upload the input data file, and verify the upload:

```bash
hdfs dfs -mkdir /tmp/USUK30/Asad
hdfs dfs -mkdir /tmp/USUK30/Asad/data
hdfs dfs -put data.txt /tmp/USUK30/Asad/data/
hdfs dfs -ls /tmp/USUK30/Asad/data
```

## Step 7: Execute MapReduce Job

Submit the MapReduce job to the Hadoop cluster using the `hadoop jar` command:

```bash
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper "/usr/bin/python mapper.py" \
-reducer "/usr/bin/python reducer.py" \
-input /tmp/USUK30/Asad/data/data.txt \
-output /tmp/USUK30/Asad/output
```

## Step 8: Check Output

Verify that the job has completed successfully and inspect the output:

```bash
hdfs dfs -ls /tmp/USUK30/Asad/output
hdfs dfs -cat /tmp/USUK30/Asad/output/part-00000
```

Congratulations! You have successfully executed a MapReduce job in the Hadoop cluster.
```
