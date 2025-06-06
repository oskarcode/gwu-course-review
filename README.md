# GWU Course Review

## Overview
A course review application designed for George Washington University students. This project provides a platform for students to share experiences, rate courses, and help peers make informed decisions about their academic choices.

## Features
- **Course Ratings**: Comprehensive rating system for courses
- **Student Reviews**: Detailed reviews from actual students
- **Search & Filter**: Find courses by department, difficulty, or professor
- **User Authentication**: Secure student login system
- **Database Integration**: Persistent storage of reviews and ratings
- **University Specific**: Tailored for GWU course catalog

## Technologies Used
- **Python** - Backend development
- **Flask/Django** - Web framework
- **SQLite/PostgreSQL** - Database management
- **HTML/CSS/JavaScript** - Frontend interface
- **Bootstrap** - Responsive design
- **Database Models** - Course and review data structures

## Project Structure
```
gwu-course-review/
├── app/                # Application code
├── models/             # Database models
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
- GWU student email for authentication

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/oskarcode/gwu-course-review.git
   cd gwu-course-review
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Features in Detail

### Course Rating System
- **Overall Rating**: 1-5 star rating system
- **Difficulty Level**: Course difficulty assessment
- **Workload**: Time commitment estimation
- **Professor Rating**: Instructor-specific feedback

### Review Categories
- **Course Content**: Quality and relevance of material
- **Teaching Quality**: Instructor effectiveness
- **Assignment Load**: Homework and project workload
- **Exam Difficulty**: Test and quiz assessment
- **Recommendation**: Would recommend to others

### Search & Discovery
- Filter by department (CS, MATH, ENG, etc.)
- Sort by rating, difficulty, or recency
- Search by course code or title
- Professor-specific reviews

## Database Schema

### Course Model
```python
class Course:
    course_code = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=50)
    credits = models.IntegerField()
    description = models.TextField()
```

### Review Model
```python
class Review:
    course = models.ForeignKey(Course)
    student = models.ForeignKey(User)
    rating = models.IntegerField(1, 5)
    difficulty = models.IntegerField(1, 5)
    workload = models.IntegerField(1, 5)
    content = models.TextField()
    semester = models.CharField(max_length=20)
```

## Contributing

### For GWU Students
1. Create an account with your GWU email
2. Search for courses you've taken
3. Leave honest, constructive reviews
4. Rate courses on multiple criteria

### For Developers
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Privacy & Guidelines
- **Anonymous Reviews**: Student identities are protected
- **Constructive Feedback**: Focus on helpful, specific feedback
- **No Personal Attacks**: Reviews should critique courses, not individuals
- **Academic Integrity**: No sharing of specific exam questions or answers
- **Moderation**: Reviews are moderated for appropriateness

## Deployment
The application can be deployed on:
- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS hosting option
- **AWS**: Scalable cloud deployment
- **Local Server**: Campus server deployment

## Future Features
- Mobile app development
- Professor response system
- Course recommendation engine
- Integration with GWU course catalog API
- Advanced analytics and insights

## License
This project is intended for educational use by GWU students and is available under the [MIT License](LICENSE).

## Support
For technical issues or feature requests:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

## Disclaimer
This is an independent project not officially affiliated with George Washington University. Reviews reflect individual student opinions and experiences.

## Contact
- GitHub: [@oskarcode](https://github.com/oskarcode)
- Project Link: [https://github.com/oskarcode/gwu-course-review](https://github.com/oskarcode/gwu-course-review)

## Acknowledgments
- GWU student community for feedback and testing
- Course review platforms for inspiration
- Open source community for tools and libraries

---
*Helping GWU students make informed course decisions*