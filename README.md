# Set up

.env setup

```
SUPABASE_URL=https://your-supabase-url.supabase.co
SUPABASE_ANON_KEY=your-anon-key
```

Create Virtual Environment

```
python3 -m venv .venv
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
