FROM mydockerhublogin/win2k16-ruby:1.0
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
ADD . /app
# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable
ENV NAME World
RUN powershell -Command \
    $ErrorActionPreference = 'Stop'; \
  New-Item "HKLM:\Software\WOW6432Node\ExampleCom" -Force ; \
  New-ItemProperty "HKLM:\Software\WOW6432Node\ExampleCom" -Name MenuLastUpdate -Value "test" -Force
RUN powershell -Command \
    $ErrorActionPreference = 'Stop'; \
  New-Item "HKLM:\Software\ExampleCom" -Force ; \
  New-ItemProperty "HKLM:\Software\ExampleCom" -Name MenuLastUpdate -Value "test" -Force
# Run ruby script when the container launches
CMD ["C:/Ruby23-x64/bin/ruby.exe", "docker_ruby_test.rb"]