const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const alertBoxEduc = document.getElementById('alert-box-educ')
const alertBoxLC = document.getElementById('alert-box-lc')
const alertBoxOther = document.getElementById('alert-box-other')
const partnerID = document.getElementById('partner-id').value
const mediaEduc = document.getElementById('media_files')
const mediaFiles = document.getElementById("inside-tbody")


firstTR = `
        <tr>
            <th>
            </th>
            <th>File Name</th>
            <th>Uploaded At</th>
            <th>Format</th>
            <th>Action</th>
        </tr>
    `

Dropzone.autoDiscover = false

const handleEducAlerts = (type, msg) => {
    alertBoxEduc.innerHTML = `
        <div class="alert alert-${type}">
            ${msg}
        </div>
    `
}

const handleLCAlerts = (type, msg) => {
    alertBoxLC.innerHTML = `
        <div class="alert alert-${type}">
            ${msg}
        </div>
    `
}

const handleOtherAlerts = (type, msg) => {
    alertBoxOther.innerHTML = `
        <div class="alert alert-${type}">
            ${msg}
        </div>
    `
}

const handleShowMedia = (data) => {

    html = ''
    for (i=0; i<data.length; i++) {
        html += `
            <p>${data[i].fields.media_filename}</p>
        `     
    }
    mediaEduc.innerHTML = html
}

const handleBadge = (format) => {
    if (format == 1) {
        return 'info'
    }
    if (format == 2) {
        return 'success'
    }
    if (format == 3) {
        return 'warning'
    }
}

const handleFormat = (format) => {
    if (format == 1) {
        return 'JPG'
    }
    if (format == 2) {
        return 'PNG'
    }
    if (format == 3) {
        return 'PDF'
    }
}

const handleDateFormat = (dateTime) => {
    return dateTime.slice(0, 10)
}

const handleFileName = (filename) => {
    return filename.split('.').slice(0, -1).join('.').slice(0, 5)
}

const handleMediaFiles = (data, type) => {
    
    html = ''
    if (type == 'ed') {
        
        for (i=0; i<data.length; i++) {
            html += `
                <tr>
                    <td class="p-0 text-center text-muted">
                        ED
                    </td>

                    <td>${handleFileName(data[i].fields.media_filename)}</td>
                    
                    <td>${handleDateFormat(data[i].fields.created)}</td>

                    <td><div class="badge badge-${handleBadge(data[i].fields.media_format)}">${handleFormat(data[i].fields.media_format)}</div></td>

                    <td><a href="#" class="btn btn-secondary">Preview</a></td>

                </tr>
            `     
        }
    }

    mediaFiles.innerHTML = firstTR + html
}

const uploadEducDropzone = new Dropzone('#educdropzone', {
    url: '/crm/educ_media_upload/',
    init: function() {
        this.on('sending', function(file, xhr, formData) {
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
            formData.append('partner_id', partnerID)
            formData.append('file_format', file.type)
        })
        this.on('success', function(file, response){
            const ex = response.ex
            const ey = JSON.parse(response.ey)
            if (ex) {
                handleEducAlerts('danger', 'File already exist!')
            } else {
                handleEducAlerts('success', 'File uploaded sucessfully!')
            }
            
            handleMediaFiles(ey, 'ed')
            
        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.png, .jpg, .jpeg, .pdf',
})


const uploadLCDropzone = new Dropzone('#lcdropzone', {
    url: '/crm/lc_media_upload/',
    init: function() {
        this.on('sending', function(file, xhr, formData) {
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
            formData.append('partner_id', partnerID)
        })
        this.on('success', function(file, response){
            const ex = response.ex
            if (ex) {
                handleLCAlerts('danger', 'File already exist!')
            } else {
                handleLCAlerts('success', 'File uploaded sucessfully!')
            }
        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.png, .jpg, .jpeg, .pdf',
})


const uploadOtherDropzone = new Dropzone('#otherdropzone', {
    url: '/crm/other_media_upload/',
    init: function() {
        this.on('sending', function(file, xhr, formData) {
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
            formData.append('partner_id', partnerID)
        })
        this.on('success', function(file, response){
            const ex = response.ex
            if (ex) {
                handleOtherAlerts('danger', 'File already exist!')
            } else {
                handleOtherAlerts('success', 'File uploaded sucessfully!')
            }
        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.png, .jpg, .jpeg, .pdf',
})