-- user definition

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	username VARCHAR(80) NOT NULL,
	password VARCHAR(120) NOT NULL
    role VARCHAR(20) DEFAULT 'User',
	description VARCHAR(200),
	UNIQUE (username)
);

-- agent_config definition 
CREATE TABLE agent_config (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    provider VARCHAR(80) NOT NULL,
    api_key VARCHAR(200),
    base_url VARCHAR(100),
    description VARCHAR(200),
    editable BOOLEAN DEFAULT 0,
    UNIQUE (provider)
);


-- user
INSERT INTO "user"
(username, password, description)
VALUES('admin', '$2b$12$MpsCfV2f1iQgXbmGdQSeq.CphpK.5xoyG8HNlhRUB.4Ae8tT4l62S', 'Administrator', 'Admin user with full access');

-- agent_config
INSERT INTO agent_config
(provider, api_key, base_url, editable, description)
VALUES('OpenAI', 'your_openai_api_key', 'https://api.openai.com/v1', 0, 'OpenAI API configuration');

INSERT INTO agent_config
(provider, api_key, base_url, editable, description)
VALUES('DeepSeek', 'your_deepseek_api_key', 'https://api.deepseek.com', 0, 'DeepSeek OpenAI API configuration');


INSERT INTO agent_config
(provider, api_key, base_url, editable, description)
VALUES('Custom', 'your_custom_api_key', 'https://api.customer.com', 1, 'Customer OpenAI API configuration');