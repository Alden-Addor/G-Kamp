# G-Kamp
PDX Code Guild Capstone Project

### PDX Capstone / Alden Addor

## Overview

The goal of this program is to be able to search, look at, and make reservations for goverment sponsered campgrounds.  Currently Recreation.gov(REC.gov) does this, but it is a difficult site navigate because it has so much on it.  It is the site for all things government recreation and I want to create something that is just camping.  I will be using their API to build out a site using Django and Vue, with Materialize as a CSS framework and Leaflet API for a interactive map.

## Features

-User signup, login, and authentication
-Search filter by state, city, National/State parks.
-Ability to put in dates of stay in search.
-Display search results on interactive map.
-Once campground is selected, display campsites as cards with pictures of the campsites and site info.
-Able to click on campsite to make reservation.
-Clicking to make reservation will redirect to the campsite reservation on REC.gov.

## Data Model

I will create a user system, storing users information such as:
-Name
-Email
-Address
-Phone Number

The REC.gov API is massive with campsites having no shortage in information about them.  I will need to store dated based on search, so I will need:
-State
-Campground
-Campsite

## Schedule

### Milestone 1 - Week 1
Create a MVP which displays a list of campgrounds based on search with the ability to click on the campground as see basic campsites info.  The user database with be built as part of this.

### Milestone 2 - Week 2
Begin creating the interactive map display with the campgrounds.  If this proves to be to much, start building out the cards for campsites with more information and user interaction linked.

### Milestone 3 - Week 3
Create the ability to link to the REC.gov reservation system with the site selected ready to reserve.