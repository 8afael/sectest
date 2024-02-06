
describe("Arachni Report", function () {

    beforeEach(function () {
        cy.visit('http://172.17.0.3:9292');
        cy.get('#user_email').type('admin@admin.admin');
        cy.get('#user_password').type('administrator');
        cy.get('.btn').click();
      });
    
      it("Save Report", function () {
        // if (cy.get("#activities").should('be.visible')) {
        //   cy.get('link=HTML').click({force:true})
        //   //cy.get('download-report > ul.nav.nav-list > li > a').click({force:true})
        //   const currentDate = new Date();
        //   const formattedDate = `${currentDate.getFullYear()}-${(currentDate.getMonth() + 1).toString().padStart(2, '0')}-${currentDate.getDate().toString().padStart(2, '0')} ${currentDate.getHours().toString().padStart(2, '0')}:${currentDate.getMinutes().toString().padStart(2, '0')}`;
        //   // cy.task('downloadZipFile', {
        //   //   url: 'http://172.17.0.3:9292/scans/1/report.html',
        //   //   filePath: 'e2e/report_Arachni_'+formattedDate+'.zip'
        //   // }).then(success => {
        //   //   if (success) {
        //   //     // File downloaded successfully, continue with assertions or further actions
        //   //     cy.log('File downloaded successfully');
        //   //   } else {
        //   //     // Handle error if file download fails
        //   //     cy.log('File download failed');
        //   //   }
        //   // });
        // }else {
          cy.intercept('/scans/*').as('scans')
          cy.visit('http://172.17.0.3:9292/scans/new');
          cy.get('#scan_url').type('http://172.17.0.2');
          cy.get('#go-btn').scrollIntoView();
          cy.get('#go-btn').should('be.visible').click();
          cy.wait(120000) 

          //cy.get('#download-report > .nav > :nth-child(1) > a').as('downloadLink')
          // cy.wait('@scans')
          cy.get('#download-report > .nav > :nth-child(1) > a').click({ download: true }, {force: true})
          
          
        //   cy.contains('a', 'report').click(({ download: true }, {force: true})).then(() => {
        //     cy.wait(5000);
          //cy.get('a[href="/scans/1/report.html"]').click({ download: true }, {force: true}).then(() => {
            // Wait for download completion (adjust timeout as needed)
           
        })
        // cy.request('http://172.17.0.3:9292/scans/1/report.html')
        //   .then((response) => {
        //     if (response.status == 200) {
        //       cy.request ({
        //       url: 'http://172.17.0.3:9292/scans/1/report.html',
        //       encoding: 'binary',
        //       method: 'GET',
        //       responseType: 'arrayBuffer',
        //     }).then((response) => {
        //       cy.writeFile('/e2e/report_Arachni_'+formattedDate+'.zip', response.body, 'binary');
              
        //     })
        //   } else {
        //     cy.wait(20000)
        //   }
        // })

   

    //   it('Download file', () => {
    //     const currentDate = new Date();
    //     const formattedDate = `${currentDate.getFullYear()}-${(currentDate.getMonth() + 1).toString().padStart(2, '0')}-${currentDate.getDate().toString().padStart(2, '0')} ${currentDate.getHours().toString().padStart(2, '0')}:${currentDate.getMinutes().toString().padStart(2, '0')}`;
    //     cy.task('downloadZipFile', {
    //       url: 'http://172.17.0.3:9292/scans/1/report.html',
    //       filePath: 'e2e/report_Arachni_'+formattedDate+'.zip'
    //     }).then(success => {
    //       if (success) {
    //         // File downloaded successfully, continue with assertions or further actions
    //         cy.log('File downloaded successfully');
    //       } else {
    //         // Handle error if file download fails
    //         cy.log('File download failed');
    //       }
    //     });
    //   })    
     })

  