https://www.geeksforgeeks.org/how-to-install-and-run-apache-kafka-on-windows/
https://stackoverflow.com/questions/47677549/kafka-zookeeper-connection-to-node-1-could-not-be-established-broker-may-no

.\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test.\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092

.\kafka-console-producer.bat --broker-list localhost:9092 --topic test

.\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test --from-beginning

./kafka-run-class.bat kafka.tools.DumpLogSegments --deep-iteration --print-data-log --files /temp/kafka-logs/test-0/00000000000000000000.log