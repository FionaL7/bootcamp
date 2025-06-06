# Day 0 - Tasks

## Server Setup (ex-tools-1)

A web server with just one page displaying my name and photo.

Used **Google Cloud VM** and **Nginx** to run the server.

**Link:** [http://mybootcamp.strangled.net/](http://mybootcamp.strangled.net/)  




## 🛠️ Tools Used

- **Google Cloud Platform (Compute Engine)**
- **Nginx Web Server**
- **afraid.org (FreeDNS)**
- **ChatGPT and Google** 

---

## 🧭 Steps Followed

1. Set up a **Virtual Machine (Debian OS)** on Google Cloud using Compute Engine.
2. Installed Nginx:
   ```bash
   sudo apt update
   sudo apt install nginx
   ```
3. Created index.html containing my name and photo.
4. Uploaded the HTML and image to:

```bash
/var/www/html/
```
5. Set up a free subdomain using afraid.org, pointing it to my external IP address.

## 🌐 Website Live At
- IP Address: http://34.136.54.235 
- Domain: [http://mybootcamp.strangled.net/](http://mybootcamp.strangled.net/) 

## 🤖 ChatGPT Help
Used ChatGPT to resolve: 
- Nginx setup
- SSH terminal navigation

# ex-basics

# fiona-hello
A simple Python CLI package that greets users using `typer` and prints styled output using `rich`.

## 📦 Install

```bash
pip install fiona-hello
```

## 🚀 Usage

```bash

say-hello --name Fiona
```

## 💡 Features

- CLI built with typer
- Beautiful output using rich
- Easy to install and run

## 🔗 PyPI Link

**Link:** [fiona-hello on PyPI](https://test.pypi.org/project/fiona-hello/0.1.2/)
