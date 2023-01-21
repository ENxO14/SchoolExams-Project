import { Observable } from "rxjs";
import { UserService } from "../user.service";
import { User } from "../user";
import { Component, OnInit } from "@angular/core";
import { Router } from '@angular/router';
import {Location} from '@angular/common'

@Component({
  selector: 'app-verif-sci-list',
  templateUrl: './verif-sci-list.component.html',
  styleUrls: ['./verif-sci-list.component.css']
})
export class VerifSciListComponent implements OnInit {
  data: User[] = undefined!;
  obsRooms: Observable<User[]> | undefined


  constructor(private userService: UserService, private router: Router, private location: Location) { }

  ngOnInit() {
    this.reloadData();
  }

  reloadData() {
    this.obsRooms = this.userService.getverifSciList()
    this.obsRooms.subscribe(this.fati)
  }
  fati = (data: User[]) => {
    this.data = data;
  }


  deleteverifSci(id: string) {
    this.userService.deleteverifSci(id)
      .subscribe(
        data => {
          console.log(data);
          this.reloadData();
        },
        error => console.log(error));
  }
  updateverifSci(id: string) {
    this.router.navigate(['verifSciupdate', id]);
  }
  back(): void {
    this.router.navigate(['/dashboard']);
  }
}