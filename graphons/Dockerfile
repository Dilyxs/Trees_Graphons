# Use the official graph-tool Docker image
FROM tiagopeixoto/graph-tool

# Set up a working directory inside the container
WORKDIR /workspace

# Install Jupyter Notebook (if not already installed)

# Expose Jupyter Notebook port
EXPOSE 7890

# Start Jupyter Notebook when the container runs
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=7890", "--no-browser", "--allow-root", "--notebook-dir=/workspace"]

#docker build -t graph-tools .

#docker run -it --rm -p 7890:7890 -v "$(pwd):/workspace" --name graph-notebook graph-tools

