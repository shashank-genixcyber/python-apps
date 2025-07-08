# Base our app image off of the WALKOFF App SDK image
FROM frikky/shuffle:app_sdk as base
 
# Create builder stage for pip installations
FROM base as builder
 
# Install build tools required by python-ldap and SASL support
RUN apk --no-cache add --update \
    alpine-sdk \
    libffi-dev \
    openssl-dev \
    python3-dev \
    musl-dev \
    openldap-dev \
    libsasl \
    git
 
# Prepare install directory
RUN mkdir /install
WORKDIR /install
 
# Copy and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --prefix="/install" -r /requirements.txt
 
# Switch back to base image
FROM base
 
# Copy installed packages and app source
COPY --from=builder /install /usr/local
COPY src /app
 
# Install runtime dependencies (includes openldap for python-ldap)
RUN apk --no-cache add --update \
    jq \
    git \
    curl \
    openldap \
    libsasl
 
# Set working directory and start the app
WORKDIR /app
CMD ["python", "app.py", "--log-level", "DEBUG"]