module.exports = {
    apps: [
      {
        name: 'BOT_FLASK',
        script: './app.py',
        instances: 1,
        autorestart: true,
        watch: false,
      },
    ],
  };
  