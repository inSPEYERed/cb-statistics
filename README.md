# Commons Booking Statistics 📊

This Python script will help you to get some statistics based on your [Commons Booking](https://github.com/wielebenwir/commonsbooking) data. The source code is only intended as a starting point to do your own evaluation (see the file `evaluation.py`). You might have to adjust the code to make it work for your specific dataset, but only small adjustments should be required (e.g. something like: add more colors to a colors array if you have more than three years of data or change the names of your bookable items).

This project is especially helpful if you want to skip the annoying parsing part of the weird database tables `posts` and `postmeta` — where the new Commons Booking (starting with version 2) is storing all of the bookings and corresponding data (instead of their lovely old, *separate* cb_tables beforehand) ...

## Usage

Tested with Python 3.10.5:

- Clone this repo: `git clone https://github.com/inSPEYERed/cb-statistics.git`.
- Install the Python requirements: `pip install -r requirements.txt`.
- In PhpMyAdmin, export the tables `<prefix>_posts` and `<prefix>_postmeta` as JSON files and put them in the `./data/` folder of this project.
- Create a `.env` file next to this Readme with the only entry `WP_TABLE_PREFIX=<your-table-prefix, e.g. wp>`.
- Run the script via `python ./src/main.py`.
- Check the folder `./plots/` to find the output (`statistics.pdf` has all the statistics combined).


## Sample result

Currently supported plots:

- Bookings per calender week
- Bookings per weekday
- Bookings per item

This is how the bookings per weekday result can look like:

![cb-statistics-sample-result](https://user-images.githubusercontent.com/37160523/182097721-954bf314-1f5b-45e9-ab38-266df26de06a.jpg)


## License

This program is licensed with the very permissive MIT license, see the LICENSE file for details. As this is only a small project, we don't require you to include the license header in every source file, however you must include it at the root of your project. According to the MIT license you must also include a copyright notice, that is, link back to this project, e.g. in this way:

cb-statistics - Copyright (c) 2022 inSPEYERed

Any questions regarding the license? [This FAQ](https://www.tawesoft.co.uk/kb/article/mit-license-faq) might help.

This project is not endorsed by the official [Commons Booking](https://github.com/wielebenwir/commonsbooking).
