mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"diegoandres.bravobecerra@outlook.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
base = 'light'\n\
\n\
" > ~/.streamlit/config.toml