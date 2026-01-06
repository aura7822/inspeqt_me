async function loadjobs(){
    const keyword = document.getElementById("keyword").value;
    let url="/jobs/recent";
    if(keyword){
        url += "?keyword="+encodeURLComponet(keyword);
    }
    const res=awaitfetch(url);
    const jobs=awaitres.json();

    const container=document.getElementById("jobs");
    container.innerHTML="";

    if(jobs.length===0){
        container.innerHTML="<p>Sorry no jobs found </p>";
        return;
    }
    jobs.forEach(job=>{
        const div= document.createElement("div");
        div.className="job";
        
        div.innerHTML=`
        <h3>${job.title}</h3>
        <p>${job.company}*${job.location}</p>
        <a href="${job.url}"target="_blank">Apply</a>
        `;

        container.appendChild(div);
    
});
}
loadjobs();