import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateVerifSciComponent } from './update-verif-sci.component';

describe('UpdateVerifSciComponent', () => {
  let component: UpdateVerifSciComponent;
  let fixture: ComponentFixture<UpdateVerifSciComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UpdateVerifSciComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UpdateVerifSciComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
