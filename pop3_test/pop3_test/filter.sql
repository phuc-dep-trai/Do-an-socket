
        CREATE TABLE IF NOT EXISTS FilterRules (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ConditionType TEXT,
            Conditions TEXT,
            TargetFolder TEXT
        );
    
                    INSERT INTO FilterRules (ConditionType, Conditions, TargetFolder)
                    VALUES ('From',' ahihi@testing.com, ahuu@testing.com', 'Project');
                
                    INSERT INTO FilterRules (ConditionType, Conditions, TargetFolder)
                    VALUES ('Subject',' urgent, ASAP', 'Important');
                
                    INSERT INTO FilterRules (ConditionType, Conditions, TargetFolder)
                    VALUES ('Content',' report, meeting', 'Work');
                
                    INSERT INTO FilterRules (ConditionType, Conditions, TargetFolder)
                    VALUES ('Spam',' virus, hack, crack', 'Spam');
                