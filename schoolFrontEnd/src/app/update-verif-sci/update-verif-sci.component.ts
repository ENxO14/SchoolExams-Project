import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../user.service';

@Component({
  selector: 'app-update-verif-sci',
  templateUrl: './update-verif-sci.component.html',
  styleUrls: ['./update-verif-sci.component.css']
})
export class UpdateVerifSciComponent implements OnInit{

  id: string = "";
  user: User = undefined!;

  constructor(private route: ActivatedRoute,private router: Router, private userService: UserService) { }

  ngOnInit() {
    this.user = new User();
    this.id = this.route.snapshot.params['id'];
    console.log("id: "+this.id)
    this.userService.getverifSci(this.id)
      .subscribe(data => {
        this.user = data;
      }, error => console.log(error));
      console.log(this.userService);
  }

  updateverifSci() {
    console.log("updateUser", this.id);
    this.userService.updateverifSci(this.id, this.user)
      .subscribe(data => {
        console.log(data);
        this.user = new User();
        this.gotoList();
      }, error => console.log(error));
  }

  

  onSubmit() {
    console.log("onSubmit")
    this.updateverifSci();     
  }

  gotoList() {
    console.log("gotoList")
    this.router.navigate(['/verifSci']);
  }
}