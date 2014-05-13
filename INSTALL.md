#Tom's Notes
To get Jekyll running on a clean Ubuntu 14.04 install, open up a terminal and enter the following.  Lines starting with # are comments and don't need to be entered.
~~~
# Install git and the ruby dev packages
sudo apt-get install git ruby1.9.1-dev  

# Install jekyll and kramdown, a particular markdown parser we're using
sudo gem install jekyll kramdown  

# Assuming you're already in a good place to put the STDIO Ghana stuff:
git clone https://github.com/pearsonca/stdio-ghana.git  

# Now change to the directory that was just created by the last command
cd stdio-ghana  

# Start up the Jekyll server
jekyll serve --watch --baseurl ""  

# Now open up a web browser, type localhost:4000 in the location bar.
# You have arrived.
~~~

#Carl Notes
On OSX 10.9, clang is configured to hard crash on options it doesn't understand.
There's an interesting discussion as to whether that makes sense or not, but to
deal with this for `gem (install|update)`s that require building something:
~~~ bash
ARCHFLAGS="-Wno-error=unused-command-line-argument-hard-error-in-future" sudo -E gem update jekyll
~~~

the `ARCHFLAGS` part is essentially telling clang to not hard crash.  The `-E`
argument to `sudo` is saying to use that environment variable.


#Jonathon's Notes
The latest version of Jekyll requires a version of Ruby that is newer than what come pre-loaded on Ubunut 14.04.  I went round and round on this and can't remember the steps or what actually worked.  I think gem might also have been needed.  I am pretty sure the command "sudo apt-get install ruby1.9.3" did something positive for my system, but your milage might vary.

Jekyll documentation should be looked at prior to use: http://jekyllrb.com/docs/usage/ The jekyll build and serve options described work well, but do not proscribe to my intuitive sense.  This resulted in complete deletion of my local git repository and creating a local website out of my entire home directory.  Fortunately, the error was easily-ish rectified.

SmartGit has a java dependency and an OOB Unbuntu install is not java-aware, even though java is loaded.  Again, I went around and around on this and am unsure what actually worked.  You might want to try "sudo update-alternatives --config java"  and look at this http://www.cs.cmu.edu/~help/unix_linux/ubuntu_java.html

PyCharm was the most trouble free.  You just unpack the .gz file into your home directory.  There are more complex instructions if you want to install it to a usr or opt. I didn't do this, but we might want to for the student machines.  I think there is a java dependency, but I didn't run into the issue once SmartGit was loaded.
