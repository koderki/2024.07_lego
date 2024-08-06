# Installation

## Raspberry Pi OS

Install dependencies
```
sudo apt-get install build-essential autoconf libncurses5-dev openssl libssl-dev fop xsltproc git
```

Install GUI dependencies
```
sudo apt-get install libwxbase3.2-1 libwxgtk3.2-dev libwxgtk-webview3.2-dev
```

Install `asdf`
```
git clone https://github.com/asdf-vm/asdf.git ~/.asdf
```

Open `.bashrc` file with `nano ~/.bashrc` and append these lines to the end
```
. “$HOME/.asdf/asdf.sh”
. “$HOME/.asdf/completions/asdf.bash”
```

Install Erlang and Elixir
```
asdf plugin add erlang
asdf plugin add elixir
asdf list-all erlang
export KERL_CONFIGURE_OPTIONS="--without-javac --without-odbc"
asdf install erlang 27.0.1
asdf global erlang 27.0.1
asdf install elixir
asdf install elixir 1.17.2-otp-27
asdf global elixir 1.17.2-otp-27
```

Install Livebook
```
mix do local.rebar --force, local.hex --force
mix escript.install hex livebook
asdf reshim elixir
```

Start Livebook server listening on a local network IP address
```
LIVEBOOK_TOKEN_ENABLED=false LIVEBOOK_IP=<Raspberry.Pi.Local.IP> livebook server
```

See all the configuration options
```
livebook server --help
```
