CREATE TABLE _user (
                       id UUID PRIMARY KEY,
                       dni_number VARCHAR(10) NOT NULL UNIQUE,
                       dni_type VARCHAR(30) NOT NULL,
                       first_name VARCHAR(50) NOT NULL,
                       last_name VARCHAR(50) NOT NULL,
                       phone_number VARCHAR(10),
                       email_address VARCHAR(70) NOT NULL UNIQUE,
                       role VARCHAR(20) NOT NULL,
                       status VARCHAR(20) NOT NULL,
                       created_at TIMESTAMP WITH TIME ZONE NOT NULL,
);

CREATE TABLE _vehicle (
                          id UUID PRIMARY KEY,
                          user_id UUID NOT NULL,
                          license_plate VARCHAR(7) NOT NULL UNIQUE,
                          model VARCHAR(50) NOT NULL,
                          vehicle_type VARCHAR(20) NOT NULL,
                          created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                          FOREIGN KEY (user_id) REFERENCES _user(id)
);

CREATE TABLE _cell (
                       id UUID PRIMARY KEY,
                       space_number VARCHAR(10) NOT NULL UNIQUE,
                       vehicle_type VARCHAR(20) NOT NULL,
                       status VARCHAR(20) NOT NULL,
                       created_at TIMESTAMP WITH TIME ZONE NOT NULL
);

CREATE TABLE _reservation (
                              id UUID PRIMARY KEY,
                              user_id UUID NOT NULL,
                              cell_id UUID NOT NULL,
                              vehicle_id UUID NOT NULL,
                              reservation_code VARCHAR(10) UNIQUE,
                              status VARCHAR(20) NOT NULL,
                              start_time TIMESTAMP WITH TIME ZONE NOT NULL,
                              end_time TIMESTAMP WITH TIME ZONE,
                              created_at TIMESTAMP WITH TIME ZONE NOT NULL,
                              FOREIGN KEY (user_id) REFERENCES _user(id),
                              FOREIGN KEY (cell_id) REFERENCES _cell(id),
                              FOREIGN KEY (vehicle_id) REFERENCES _vehicle(id)
);
