INSERT INTO "worldTravelCountryRegions" (id, name, country_code)
VALUES
  ('EG-ALX', 'Alexandria', 'eg'),
  ('EG-ASN', 'Aswan', 'eg'),
  ('EG-ASY', 'Asyut', 'eg'),
  ('EG-BHR', 'Beheira', 'eg'),
  ('EG-BNS', 'Beni Suef', 'eg'),
  ('EG-C', 'Cairo', 'eg'),
  ('EG-DK', 'Dakahlia', 'eg'),
  ('EG-DAM', 'Damietta', 'eg'),
  ('EG-FYM', 'Faiyum', 'eg'),
  ('EG-GH', 'Gharbia', 'eg'),
  ('EG-GZ', 'Giza', 'eg'),
  ('EG-IS', 'Ismailia', 'eg'),
  ('EG-KB', 'Kafr El Sheikh', 'eg'),
  ('EG-LX', 'Luxor', 'eg'),
  ('EG-MN', 'Minya', 'eg'),
  ('EG-MT', 'Matrouh', 'eg'),
  ('EG-QH', 'Qalyubia', 'eg'),
  ('EG-KFS', 'Qena', 'eg'),
  ('EG-SHG', 'Sohag', 'eg'),
  ('EG-SHR', 'Sharqia', 'eg'),
  ('EG-SIN', 'South Sinai', 'eg'),
  ('EG-SW', 'Suez', 'eg'),
  ('EG-WAD', 'New Valley', 'eg'),
  ('EG-ASD', 'North Sinai', 'eg'),
  ('EG-PTS', 'Port Said', 'eg'),
  ('EG-SKB', 'Suez', 'eg'),
  ('EG-ESI', 'Ismailia', 'eg')

ON CONFLICT (id) DO NOTHING;
