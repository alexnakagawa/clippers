# Clippers Developer Project

This is the repository containing all of the required materials for the Clippers developer assessment. The presentation of the supplementary answers to the Questionnaire, along with explanations to my code, can be found [here](https://docs.google.com/presentation/d/1bqit9C1NRHd7KAHez_m0dDFxFSbZEz5v2wAxjc2xvhc/edit?usp=sharing), and is also sent as a PDF attached to the email.

## Development Prerequisites and Setup

For development and uniformity purposes, there are several dependency requirements your local machine must meet. We will be using `pip` as our package manager, but the instructions stay largely the same for `conda` as well: 

### Lineups

Skip directly to the running Google Studio visualization by clicking the logo below:

[![google-studio](https://www.oogstonline.com/upload/logo/Google/lockup_ic_DataStudio_horiz_544px_clr%20VIERKANT.png)](https://datastudio.google.com/u/0/reporting/1l6Gf4Qei58CDM-9BY2KXl7Jshmr0jLQ1/page/jPKSB)

1. There is a `requirements.txt` file that lists the packages needed to run. Change the working directory to the project root `clippers` and run the following command to ensure that the requirements are met.
```{bash}
pip install -U ./lineups/requirements.txt
```
Alternatively, you can open `requirements.txt` and run the usual `pip install ...` for each package listed.

2. Run the following command to open the notebook on your own localhost: `jupyter notebook` If you don't have `jupyter core` installed, please follow the [instructions here](https://jupyter.org/install) to do so.

3. Fill in the empty strings with the variables as outlined in the separate `keys.json` file I attached to the email.

4. The setup should now be complete. Please email [alex.nakagawa@berkeley.edu](sendto:alex.nakagawa@berkeley.edu) for any troubleshooting.

### Two Way

Skip to the deployed version on Vercel's now.sh by clicking the logo below.

[![vercel](https://www.underconsideration.com/brandnew/archives/vercel_logo_before_after.png)](https://clippers-two-way.now.sh/)

1. Please ensure that you have at least `npm` version 6.14.4 or above installed globally before doing development. Instructions for install can be found [here](https://nodejs.org/en/download/).

2. Change the working directory to as follows: `cd <path_to_project_root>/two_way/app`.

3. Run `npm install`.

4. Run `npm run dev` to begin a client running on `[localhost:5000](httpp://localhost:5000)`.
