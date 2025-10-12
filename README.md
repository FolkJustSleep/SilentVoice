# Set up

.env setup

```
SUPABASE_URL=https://your-supabase-url.supabase.co
SUPABASE_SECRET_KEY=your-anon-key
ELEVENLABS_API_KEY=your-elevenlab-api-key
```

Create Virtual Environment use Python 3.11

```
python3.11 -m venv .venv
```

Activate Virtual Environment

```
source .venv/bin/activate
```

Install Dependencies

```
pip install -r requirements.txt
```

If you add more dependencies to the project use this command to update requirements.txt

```
pip freeze > requirements.txt
```

Run

```
python main.py
```
