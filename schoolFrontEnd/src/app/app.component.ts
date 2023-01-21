import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'schoolFrontEnd';

  constructor(private router: Router) {}
  
  logout() {
    // Clear session data
    localStorage.removeItem('user');

    // Redirect to login page
    this.router.navigate(['/login']);
  }

  redirect(){
    this.router.navigate(['/login']);
}
}
