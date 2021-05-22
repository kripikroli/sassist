const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
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
        <th>Actions</th>
    </tr>
`

Dropzone.autoDiscover = false

const handleAlerts = (type) => {

    if (type == 'success') {
        iziToast.success({
            title: 'File uploaded!',
            message: 'Add more by dragging files',
            position: 'topRight'
        });
    }
    else {
        iziToast.error({
            title: 'File already exist!',
            message: 'Please upload a different file',
            position: 'topRight'
        });
    }
    
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
        return 'success'
    }
    if (format == 2) {
        return 'info'
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

const handleMediaFiles = (data_ed, data_lc, data_od) => {

    console.log(data_ed)
    
    html_ed = ''
    html_lc = ''
    html_od = ''
    
    for (i=0; i<data_ed.length; i++) {
        html_ed += `
            <tr>
                <td class="p-0 text-center text-muted">
                    ED
                </td>

                <td>${handleFileName(data_ed[i].fields.media_filename)}</td>
                
                <td>${handleDateFormat(data_ed[i].fields.created)}</td>

                <td><div class="badge badge-${handleBadge(data_ed[i].fields.media_format)}">${handleFormat(data_ed[i].fields.media_format)}</div></td>

                <td>
                    <a href="?remove_ed=${data_ed[i].pk}" class="btn btn-icon btn-danger mr-2"> <i class="fas fa-times"></i> </a>
                    <a target="_blank" href="/media/${data_ed[i].fields.media_content}" class="btn btn-icon btn-light"><i class="fas fa-eye"></i> PREVIEW</a>
                </td>

            </tr>
        `     
    }

    for (i=0; i<data_lc.length; i++) {
        html_ed += `
            <tr>
                <td class="p-0 text-center text-muted">
                    LC
                </td>

                <td>${handleFileName(data_lc[i].fields.media_filename)}</td>
                
                <td>${handleDateFormat(data_lc[i].fields.created)}</td>

                <td><div class="badge badge-${handleBadge(data_lc[i].fields.media_format)}">${handleFormat(data_lc[i].fields.media_format)}</div></td>

                <td>
                    <a href="?remove_lc=${data_lc[i].pk}" class="btn btn-icon btn-danger mr-2"> <i class="fas fa-times"></i> </a>
                    <a target="_blank" href="/media/${data_lc[i].fields.media_content}" class="btn btn-icon btn-light"><i class="fas fa-eye"></i> PREVIEW</a>
                </td>

            </tr>
        `     
    }

    for (i=0; i<data_od.length; i++) {
        html_ed += `
            <tr>
                <td class="p-0 text-center text-muted">
                    OD
                </td>

                <td>${handleFileName(data_od[i].fields.media_filename)}</td>
                
                <td>${handleDateFormat(data_od[i].fields.created)}</td>

                <td><div class="badge badge-${handleBadge(data_od[i].fields.media_format)}">${handleFormat(data_od[i].fields.media_format)}</div></td>

                <td>
                    <a href="?remove_od=${data_od[i].pk}" class="btn btn-icon btn-danger mr-2"> <i class="fas fa-times"></i> </a>
                    <a target="_blank" href="/media/${data_od[i].fields.media_content}" class="btn btn-icon btn-light"><i class="fas fa-eye"></i> PREVIEW</a>
                </td>

            </tr>
        `     
    }


    mediaFiles.innerHTML = firstTR + html_ed + html_lc + html_od
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
            const data_ed = JSON.parse(response.data_ed)
            const data_lc = JSON.parse(response.data_lc)
            const data_od = JSON.parse(response.data_od)

            if (ex) {
                handleAlerts('danger')
            } else {
                handleAlerts('success')
            }
            
            handleMediaFiles(data_ed, data_lc, data_od)
            
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
            const data_ed = JSON.parse(response.data_ed)
            const data_lc = JSON.parse(response.data_lc)
            const data_od = JSON.parse(response.data_od)

            if (ex) {
                handleAlerts('danger')
            } else {
                handleAlerts('success')
            }
            
            handleMediaFiles(data_ed, data_lc, data_od)

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
            const data_ed = JSON.parse(response.data_ed)
            const data_lc = JSON.parse(response.data_lc)
            const data_od = JSON.parse(response.data_od)

            if (ex) {
                handleAlerts('danger')
            } else {
                handleAlerts('success')
            }
            
            handleMediaFiles(data_ed, data_lc, data_od)

        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.png, .jpg, .jpeg, .pdf',
})

