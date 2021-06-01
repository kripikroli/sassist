from .models import JobKeyAbout, Job, JobAbout

def get_job_abouts(job_id, job_key_about_id):
    return JobAbout.objects.filter(job_id=job_id, job_key_about_id=job_key_about_id)