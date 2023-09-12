# Hello World Collection

Collection of guides and code to print "Hello, World!" to different places.

### Motivation

The goal is to create simple examples of usage for different tools and libraries so that the function is isolated. This can hopefully be used to better understand core functionalities of these tools.

### Rules
- The program should only output hw to the specified place.
- The program should do only the minimal neccesary amount of setup for the task at hand.
- The program should follow as much of the PEP style guide as possible. 
- It should be very clear, if the program ran correctly or not. So do not write to files you have read from.
- The tasks should be somewhat challenging and not copy the whole documentation of the used libraries as such. The goal is not to use every method available to throw around greetings, but rather to provide barebone structure to build upon.
- All the steps taken should be isolated in code and properly explained. This is a learning project.
- Every task requiring particular environment should contain a readme file and information resources used should be linked in this file.
- All tasks or at least task folders should be linked in this document and briefly explained.
- Do not be afraid to break rules if it helps teaching others better.

## Contents

Sort of a table of contents for the different experiments. I am using hw as a shortcut, because this would be a lot of writing otherwise.

### The obvious place

> Hello, World!

### Python
 - [hello_world.py](https://github.com/robovo/hello-world-collection/blob/main/Python/hello_world.py) - printing to console


## The TODO list

- Python
  - [x] The first one
  - Files
    - [ ] Output to file
      - [ ] Take filename as parameter
    - [ ] Read from a file
    - [ ] Set to an ENV variable
    - [ ] Read from ENV

  - Modules
    - [ ] Using logging module
    - [ ] Write to JSON

  - Network
    - [ ] As a server request using requests module
      - [ ] Get hw from endpoint
      - [ ] Post hw to endpoint
    - [ ] As a server request using httpx module
    - [ ] Send in an E-mail subject

  - Async
    - [ ] Using async function
    - [ ] As a async server request using async httpx module
    - [ ] Async to a file

- HTML
  - A passive web page containing hw:
    - [ ] In the title
    - [ ] In the body
    - [ ] In a SVG canvas

- Flask
  - Respond to a request:
    - [ ] With plaintext hw
    - [ ] With HTML hw
      - [ ] Loaded from a file
    - [ ] With a JSON object
    - [ ] If it is properly authorized with a JWT

- Docker
  - [ ] A Docker container responding with one of the Flask examples


