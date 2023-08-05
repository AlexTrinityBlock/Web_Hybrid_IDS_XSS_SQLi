# Web_Hybrid_IDS_XSS_SQLi

This is a self-hosted API based on Tensorflow and FastAPI to detect SQL injection and XSS.

![alt text](https://raw.githubusercontent.com/AlexTrinityBlock/Web_Hybrid_IDS_XSS_SQLi/master/img/dashboard-1.jpg?raw=true)

---

# Setup

Edit .env file with right openai api key,then

```
mv .env.example .env
```

# run docker compose

```
docker-compose --env-file .env  up -d 
```

# Watch Dashboard

http://localhost:8080/