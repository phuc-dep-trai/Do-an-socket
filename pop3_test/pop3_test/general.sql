
        CREATE TABLE IF NOT EXISTS Config (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SettingName TEXT,
            SettingValue TEXT
        );
    
                    INSERT INTO Config (SettingName, SettingValue)
                    VALUES ('Username', 'Bui Hong Phuc <duyphuc2425@gmail.com>');
                    
                    INSERT INTO Config (SettingName, SettingValue)
                    VALUES ('Password', 'ahihi');
                
                    INSERT INTO Config (SettingName, SettingValue)
                    VALUES ('MailServer', '127.0.0.1');
                
                    INSERT INTO Config (SettingName, SettingValue)
                    VALUES ('SMTP', '3335');
                
                    INSERT INTO Config (SettingName, SettingValue)
                    VALUES ('POP3', '4445');
                
                    INSERT INTO Config (SettingName, SettingValue)
                    VALUES ('Autoload', '10');
                