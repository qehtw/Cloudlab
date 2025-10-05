    -- Inserting data into Users table
    INSERT INTO Users (name, phone_number, email, address) VALUES
    ('Ivan Ivanov', '0671234567', 'ivan.ivanov@example.com', 'Kyiv, Shevchenka St., 1'),
    ('Petro Petrov', '0672345678', 'petro.petrov@example.com', 'Lviv, Franka St., 2'),
    ('Olena Olenenko', '0673456789', 'olena.olenko@example.com', 'Odessa, Deribasivska St., 3'),
    ('Mykola Mykolenko', '0674567890', 'mykola.mykolenko@example.com', 'Kharkiv, Pushkina St., 4'),
    ('Anna Annenko', '0675678901', 'anna.annenko@example.com', 'Dnipro, Hrushevskoho St., 5'),
    ('Taras Tarasenko', '0676789012', 'taras.tarasenk@example.com', 'Zaporizhzhia, Sverdova St., 6'),
    ('Oleksandr Oleksandrov', '0677890123', 'oleksandr.oleks@example.com', 'Kryvyi Rih, Lenina St., 7'),
    ('Valentina Valentinenko', '0678901234', 'valentina.valentin@example.com', 'Chernivtsi, Hoholya St., 8'),
    ('Serhii Serhiyovych', '0679012345', 'serhii.serhiyovych@example.com', 'Uzhhorod, Levka St., 9'),
    ('Dmytro Dmytrenko', '0670123456', 'dmytro.dmytrenko@example.com', 'Mykolaiv, Sadova St., 10');

    -- Inserting data into Manufacturers table
    INSERT INTO Manufacturers (name) VALUES
    ('TM ABV'),
    ('TM GDE'),
    ('TM XYZ'),
    ('TM DEF'),
    ('TM GHI'),
    ('TM JKL'),
    ('TM MNO'),
    ('TM PQR'),
    ('TM STU'),
    ('TM VWX');

    -- Inserting data into Equipment table
    INSERT INTO Equipment (name, manufacturer_id) VALUES
    ('Smartphone', 1),
    ('Laptop', 2),
    ('Printer', 3),
    ('Scanner', 4),
    ('Fax', 5),
    ('TV', 6),
    ('Camera', 7),
    ('Audio System', 8),
    ('Modem', 9),
    ('Projector', 10);

    -- Inserting data into Spare_Parts table
    INSERT INTO Spare_Parts (name, manufacturer_id, quantity) VALUES
    ('Battery', 1, 20),
    ('Charger', 2, 15),
    ('Cartridge', 3, 10),
    ('Display', 4, 5),
    ('Keyboard', 5, 30),
    ('Mouse', 6, 25),
    ('Disk', 7, 12),
    ('Microphone', 8, 18),
    ('Sensor', 9, 8),
    ('Cable', 10, 50);

    -- Inserting data into Technicians table
    INSERT INTO Technicians (name, phone_number, email) VALUES
    ('Technician 1', '0681234567', 'tech1@example.com'),
    ('Technician 2', '0682345678', 'tech2@example.com'),
    ('Technician 3', '0683456789', 'tech3@example.com'),
    ('Technician 4', '0684567890', 'tech4@example.com'),
    ('Technician 5', '0685678901', 'tech5@example.com'),
    ('Technician 6', '0686789012', 'tech6@example.com'),
    ('Technician 7', '0687890123', 'tech7@example.com'),
    ('Technician 8', '0688901234', 'tech8@example.com'),
    ('Technician 9', '0689012345', 'tech9@example.com'),
    ('Technician 10', '0680123456', 'tech10@example.com');

    -- Inserting data into Repair_Types table
    INSERT INTO Repair_Types (name) VALUES
    ('Diagnostics'),
    ('Repair'),
    ('Maintenance'),
    ('Installation'),
    ('Upgrade'),
    ('Bug Fixing'),
    ('Update'),
    ('Inspection'),
    ('Cleaning'),
    ('Parts Ordering');

    -- Inserting data into User_Equipment table
    INSERT INTO User_Equipment (user_id, equipment_id, serial_number, purchase_date) VALUES
    (1, 1, 'SN001', '2023-01-15'),
    (2, 2, 'SN002', '2023-02-20'),
    (3, 3, 'SN003', '2023-03-25'),
    (4, 4, 'SN004', '2023-04-10'),
    (5, 5, 'SN005', '2023-05-05'),
    (6, 6, 'SN006', '2023-06-12'),
    (7, 7, 'SN007', '2023-07-15'),
    (8, 8, 'SN008', '2023-08-20'),
    (9, 9, 'SN009', '2023-09-25'),
    (10, 10, 'SN010', '2023-10-30');

    -- Inserting data into Repairs table
    INSERT INTO Repairs (user_equipment_id, repair_type_id, status, start_date, end_date, repairs_name) VALUES
    (1, 1, 'in_progress', '2023-11-01', NULL , 'Repair 1'),
    (2, 2, 'completed', '2023-11-02', '2023-11-10', 'Repair 2'),
    (3, 3, 'in_progress', '2023-11-03', NULL , 'Repair 3'),
    (4, 4, 'completed', '2023-11-04', '2023-11-12', 'Repair 4'),
    (5, 5, 'in_progress', '2023-11-05', NULL , 'Repair 5'),
    (6, 6, 'completed', '2023-11-06', '2023-11-13', 'Repair 6'),
    (7, 7, 'in_progress', '2023-11-07', NULL , 'Repair 7'),
    (8, 8, 'completed', '2023-11-08', '2023-11-14', 'Repair 8'),
    (9, 9, 'in_progress', '2023-11-09', NULL , 'Repair 9'),
    (10, 10, 'completed', '2023-11-10', '2023-11-15', 'Repair 10');


    -- Inserting data into Repair_Comments table
    INSERT INTO Repair_Comments (repair_id, comment) VALUES
    (1, 'This is the first comment on the repair.'),
    (2, 'Repair completed, everything is working fine.'),
    (3, 'The technician was late for the service.'),
    (4, 'Repair completed with excellent results.'),
    (5, 'The battery needs to be replaced.'),
    (6, 'Everything was done quickly and efficiently.'),
    (7, 'The modem needs to be checked again.'),
    (8, 'Repair was successfully completed.'),
    (9, 'There are minor connection issues.'),
    (10, 'Repair was completed without any issues.');

    -- Inserting data into Technician_Repairs table (associating each technician with each repair)
    INSERT INTO Technician_Repairs (technician_id, repair_id)
    SELECT technician_id, repair_id
    FROM Technicians, Repairs;

    -- Inserting data into Technician_Schedule table
    INSERT INTO Technician_Schedule (technician_id, work_day, start_time, end_time) VALUES
    (1, 'Monday', '09:00:00', '17:00:00'),
    (2, 'Tuesday', '09:00:00', '17:00:00'),
    (3, 'Wednesday', '09:00:00', '17:00:00'),
    (4, 'Thursday', '09:00:00', '17:00:00'),
    (5, 'Friday', '09:00:00', '17:00:00'),
    (6, 'Saturday', '10:00:00', '16:00:00'),
    (7, 'Sunday', '10:00:00', '16:00:00'),
    (1, 'Tuesday', '09:00:00', '17:00:00'),
    (2, 'Wednesday', '09:00:00', '17:00:00'),
    (3, 'Thursday', '09:00:00', '17:00:00');

    -- Inserting data into Replaced_Parts table
    INSERT INTO Replaced_Parts (repair_id, part_id, quantity) VALUES
    (1, 1, 1),
    (2, 2, 1),
    (3, 3, 2),
    (4, 4, 1),
    (5, 5, 1),
    (6, 6, 3),
    (7, 7, 1),
    (8, 8, 2),
    (9, 9, 1),
    (10, 10, 1);
