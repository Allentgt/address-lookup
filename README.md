###### **Address-Book Lookup Application**

This is a dockerised implementation of a simple address book lookup of data from flat files and RDBMS data sources(current implementation only supports SQLite but easily extensible to other sources as well). The implementation is done in `python 3.7`.

###### **Pre Requisites**

Make sure you have docker installed and running.

###### **Build Procedure**

* Extract the `code.zip` file to a suitable location and open a terminal at the root location(folder containing the Dockerfile).
* Run the following command to start building the local image for the app.

    `docker build -t address .`
* After the build is complete, the application can be run with the following command.

    `docker run -it address`
* Pass in the term you want to search upon the prompt.

###### **Configurations**

* All the configurations details are mentioned in the `.env` file.